# Project-MVP: CLI Password Manager

## Overview

Project-MVP is a command-line interface (CLI) password manager that allows users to securely manage their credentials. The application supports user authentication, credential management, password generation, and encryption to ensure the security of stored credentials.

## Features

- **User Authentication:** Register and login with a username and password.
- **Credential Management:** Add, retrieve, update, delete, and list credentials.
- **Password Generation:** Generate strong, random passwords.
- **Encryption:** Encrypt and decrypt stored passwords.

## Setup

### Prerequisites

- Python 3.6+
- Pipenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nickstech707/Phase-3-Project-SecureVault-App
   cd Phase-3-Project-SecureVault-App
   ```

2. **Setup virtual environment:**

   ```
   pipenv install
   ```

3. **Initialize the database:**

   ```
   pipenv run python -m app.database
   ```

4. **Generate a secret key for encryption:**
   ```
   pipenv run python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" > secret.key
   ```

## Usage

1. **Activate the virtual environment:**

   ```
   pipenv shell
   ```

2. **Run the CLI:**

   ```
   python -m app.cli
   ```

3. **Available Commands:**
   - **Register:** Create a new user account.
     ```
     python -m app.cli register
     ```
   - **Login:** Login to an existing account.
     ```
     python -m app.cli login
     ```
   - **Add Credential:** Add a new credential.
     ```
     python -m app.cli add_credential
     ```
   - **Retrieve Credential:** Retrieve an existing credential.
     ```
     python -m app.cli retrieve_credential
     ```
   - **Update Credential:** Update an existing credential.
     ```
     python -m app.cli update_credential
     ```
   - **Delete Credential:** Delete an existing credential.
     ```
     python -m app.cli delete_credential
     ```
   - **List Credentials:** List all stored credentials.
     ```
     python -m app.cli list_credentials
     ```
   - **Generate Password:** Generate a strong password.
     ```
     python -m app.cli generate_password
     ```
   - **Logout:** Logout the current user.
     ```
     python -m app.cli logout
     ```
   - **Exit:** Exit the CLI application.
     ```
     python -m app.cli exit
     ```

## Contributing

1. **Fork the repository.**
2. **Create a new branch:**
   ```
   git checkout -b my-new-feature
   ```
3. **Make your changes and commit them:**
   ```
   git commit -m 'Add some feature'
   ```
4. **Push to the branch:**
   ```
   git push origin my-new-feature
   ```
5. **Submit a pull request.**

## License

This project is licensed under the MIT License.

## Acknowledgements

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Click](https://click.palletsprojects.com/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)
- [Cryptography](https://cryptography.io/)
