
import os
import tempfile

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from resume_parser import parse_resume


app = Flask(__name__)

# Maximum upload size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSION = ".pdf"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    uploaded_file = request.files.get("resume")

    # Check whether a file was selected.
    if uploaded_file is None or not uploaded_file.filename:
        return render_template(
            "index.html",
            error="Please select a PDF resume to upload."
        ), 400

    # Secure the filename and check the extension.
    filename = secure_filename(uploaded_file.filename)

    if not filename or not filename.lower().endswith(ALLOWED_EXTENSION):
        return render_template(
            "index.html",
            error="Invalid file. Please upload a PDF resume."
        ), 400

    temporary_path = None

    try:
        # Create a temporary file safely.
        with tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".pdf",
            delete=False
        ) as temporary_file:
            temporary_path = temporary_file.name
            uploaded_file.save(temporary_file)

        # Extract information from the PDF.
        result = parse_resume(temporary_path)

        return render_template(
            "result.html",
            result=result,
            filename=filename
        )

    except ValueError as error:
        return render_template(
            "index.html",
            error=str(error)
        ), 400

    except Exception:
        app.logger.exception("Resume processing failed.")

        return render_template(
            "index.html",
            error="Something went wrong while processing the resume."
        ), 500

    finally:
        # Delete the temporary file after processing.
        if temporary_path and os.path.exists(temporary_path):
            try:
                os.remove(temporary_path)
            except OSError:
                app.logger.warning(
                    "Could not delete temporary resume file."
                )


@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        error="The PDF is too large. Maximum allowed size is 5 MB."
    ), 413


if __name__ == "__main__":
    app.run(debug=True)

