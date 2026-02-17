# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

### GitHub Pages deployment (static rewrite)

This repo now includes a static HTML/CSS/JS version that can be hosted on
GitHub Pages. The entry point is index.html and it loads data from data/elements.json.

1. Commit the static files

   ```
   index.html
   styles.css
   app.js
   data/elements.json
   ```

2. Enable GitHub Pages

   - Go to Settings -> Pages.
   - Under Build and deployment, select Deploy from a branch.
   - Choose the branch (usually main) and the root folder (/).
   - Save.

3. Visit your site

   GitHub will provide a URL like:
   https://<your-username>.github.io/<your-repo>/
