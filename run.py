import os
from taskmanager import app

if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 to make it accessible from outside the container
    # The port defaults to 5000 if the PORT environment variable is not set
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 5000)),
        # Enable debug mode for development (be cautious about using this in production)
        debug=True
    )
