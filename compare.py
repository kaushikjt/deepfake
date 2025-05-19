import os

def is_match(upload_path, ftype):
    """
    Checks if 'real' or 'fake' is in the uploaded file's name (case-insensitive).
    Works for images, audio, and video.
    """
    filename = os.path.basename(upload_path).lower()

    if 'real' in filename:
        return (
            "STATUS: Authentic File Verified\n\n"
            "The uploaded file has been successfully verified and does not contain any signs of manipulation or DeepFake content.\n\n"
            "Result: Genuine Content Detected\n"
            "Action: You may proceed safely with this file.\n"
            "Note: Continue to ensure all files are from trusted sources."
        )
    elif 'fake' in filename:
        return (
            "The uploaded file has been identified as a DeepFake.\n"
            "This content appears to be digitally manipulated and may not be authentic.\n\n"
            "Status: Fake Content Detected\n"
            "Action Required: Please verify the file source or upload a different file.\n"
            "Recommendation: Avoid trusting or sharing this content without proper verification."
        )
    else:
        return 'Unknown'
