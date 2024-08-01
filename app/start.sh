!/bin/sh

echo ""
echo "Loading azd .env file from current environment"
echo ""

if [ $? -ne 0 ]; then
    echo "Failed to load environment variables from azd environment"
    exit $?
fi

cd ../
echo 'Creating python virtual environment ".venv"'
python3 -m venv .venv

echo ""
echo "Restoring backend python packages"
echo ""

./.venv/Scripts/python -m pip install -r app/backend/requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to restore backend python packages"
    exit $?
fi

# echo ""
# echo "Restoring frontend npm packages"
# echo ""

# cd app/frontend
# npm install
# if [ $? -ne 0 ]; then
#     echo "Failed to restore frontend npm packages"
#     exit $?
# fi

# echo ""
# echo "Building frontend"
# echo ""

# npm run build
# if [ $? -ne 0 ]; then
#     echo "Failed to build frontend"
#     exit $?
# fi

# echo ""
# echo "Starting backend"
# echo ""

# cd ../backend

cd app/backend

port=5000
host=localhost
../../.venv/Scripts/python -m quart --app main:app run --port "$port" --host "$host" --reload
if [ $? -ne 0 ]; then
    echo "Failed to start backend"
    exit $?
fi
