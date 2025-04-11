# Climate Change Analyzer

This project provides data processing and analytical tools for climate change data. It includes scripts for analyzing climate-related disasters, generating predictions, and running various algorithms. The setup and execution of the project can be automated using the `init.sh` script.

## Setup Instructions

### 1. Set Up the Virtual Environment

Before running the project, you need to set up the virtual environment. If you haven't created one already, do so by running the following:

```bash
python3 -m venv venv
```

To activate the virtual environment, run:

```bash
source venv/bin/activate
```

When you're done working on the project, you can deactivate the virtual environment using:

```bash
deactivate
```

### 2. Install Dependencies

Ensure all required Python packages are installed by running the following:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Environment

To ensure the scripts can properly reference the `src` directory, set the `PYTHONPATH` environment variable:

```bash
export PYTHONPATH=src
```

### 4. Running the Project

You have two options to run the project:

#### Option 1: Running the Project Using `init.sh`

You can automate the entire setup, execution, and testing process by using the `init.sh` script. This script will:

- Set up the virtual environment
- Install dependencies
- Create necessary directories
- Run all relevant Python scripts
- Run unit tests to ensure everything works correctly

To use `init.sh`, run the following command from the root project directory:

```bash
./init.sh
```

#### Option 2: Running the Scripts Manually

Alternatively, you can manually run the scripts in the `src` directory for data processing and analysis. Navigate to the `src` directory and execute the processing and analysis scripts in order:

```bash
cd src
python3 data_processor.py
python3 algorithms.py
python3 multi_algorithms.py
python3 time_series.py
python3 clust.py
cd ..
```

### 5. Running Unit Tests

To ensure that the scripts are functioning correctly, run the unit tests:

```bash
python3 -m unittest
```

### 6. Viewing Informational Website: 
### 6. Viewing Informational Website
To view the informational website locally, follow these steps:

1. Navigate to the `frontend` directory:
   ```bash
   cd src/frontend/
   ```

2. Install the necessary dependencies:
    ```bash
    npm install
    ```
    If you encounter issues with the node_modules folder, you can delete it and reinstall the dependencies:
    ``` bash
    rm -rf node_modules/
    npm install
    ```
3. Start the development server:
    ```bash
    npm run dev
    ```
4. A link will be given that you can click to view!

### Notes

- Ensure all dependencies in `requirements.txt` are installed before running the scripts.
- The `init.sh` script automates the process of setting up and running the project. If you prefer manual execution, follow the instructions in Option 2.
- The generated data will be stored in the `data/generated_data` directory, and images in the `data/generated_data/images` directory.

### Directory Structure

The project's directory structure should look like this:

```
├── data/
│   └── generated_data/
│       └── images/
├── src/
│   ├── frontend/
│   ├── data_processor.py
│   ├── algorithms.py
│   ├── multi_algorithms.py
│   ├── time_series.py
│   └── clust.py
├── tests/
├── requirements.txt
├── init.sh
└── README.md
```
