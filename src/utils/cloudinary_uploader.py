# src/utils/cloudinary_uploader.py
from fastapi import UploadFile, HTTPException
import cloudinary.uploader
from cloudinary.exceptions import Error as CloudinaryError

def upload_image(file: UploadFile, folder: str):
    """
    Mengunggah file gambar ke Cloudinary.

    :param file: File yang diunggah dari request FastAPI (UploadFile).
    :param folder: Nama folder di Cloudinary untuk menyimpan gambar.
    :return: URL gambar yang aman (https).
    """
    try:
        # Mengunggah file ke Cloudinary
        upload_result = cloudinary.uploader.upload(
            file.file,         # Ambil file object dari UploadFile
            folder=folder,     # Tentukan folder di Cloudinary
            resource_type="image"
        )
        # Ambil URL yang aman (https) dari hasil upload
        secure_url = upload_result.get("secure_url")
        if not secure_url:
            raise HTTPException(status_code=500, detail="Failed to get secure URL from Cloudinary")

        return secure_url

    except CloudinaryError as e:
        # Tangani error spesifik dari Cloudinary
        raise HTTPException(status_code=500, detail=f"Cloudinary upload failed: {e}")
    except Exception as e:
        # Tangani error umum lainnya
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred during file upload: {e}")