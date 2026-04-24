from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import pillow_avif
import io
import os

app = FastAPI()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/convert")
async def convert_image(
    file: UploadFile = File(...),
    quality: int = Form(80)
):
    # Validate file type
    content_type = file.content_type
    if content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(status_code=400, detail="Only JPG, PNG, and WebP images are supported.")

    try:
        # Read image
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        
        # Prepare output buffer
        output = io.BytesIO()
        
        # Convert to AVIF
        img.save(output, format="AVIF", quality=quality)
        output.seek(0)
        
        # Generate filename
        original_filename = os.path.splitext(file.filename)[0]
        new_filename = f"{original_filename}.avif"
        
        return StreamingResponse(
            output, 
            media_type="image/avif",
            headers={"Content-Disposition": f"attachment; filename={new_filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {str(e)}")

# This allows running locally with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
