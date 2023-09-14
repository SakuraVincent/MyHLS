from dotenv import load_dotenv

load_dotenv()

import schedule
from views import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6635, debug=True)
