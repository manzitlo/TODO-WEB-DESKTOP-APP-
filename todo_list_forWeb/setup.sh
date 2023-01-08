# Create a new directory
mkdir -p ~/.streamlit/

# create files and folders
echo "\
[general]\n\
email = \"email@domain\"\n\
" > ~/.streamlit/credentials.toml


echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml