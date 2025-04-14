# Code-Test Generator

This Python script automatically generates concise functions along with corresponding test cases using Azure's GPT models integrated via the LangChain library.

## 🚀 Features

- ✅ Automatically generates code snippets based on provided tasks.
- ✅ Generates appropriate test cases for the created functions.
- ✅ Customizable through command-line arguments.
- ✅ Seamlessly integrates with AzureChatOpenAI.

## 📦 Installation

Follow these steps to set up the project:

### 1. Clone the repository:

```bash
git clone <your_repo_url>
cd <your_repo_name>
```

### 2. Install dependencies:

```bash
pip install langchain langchain_openai python-dotenv
```

### 3. Configure API endpoint:

Create a `.env` file in the root directory of the project:

```bash
OPENAI_BASE_URL=<your_openai_base_url>
```

## 💻 Usage

Run the script with customizable arguments:

```bash
python script.py --task "return a list of even numbers from 1 to 10" --language python
```

### Default values:

- **Task:** `return a list of numbers`
- **Language:** `python`

## 🔍 Example Output

```bash
Generated Code:
def get_even_numbers():
    return [num for num in range(1, 11) if num % 2 == 0]

Generated Test:
import unittest

class TestGetEvenNumbers(unittest.TestCase):
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers(), [2, 4, 6, 8, 10])

if __name__ == "__main__":
    unittest.main()
```

## 📁 Project Structure

```plaintext
├── .env
├── script.py
├── config.py
├── requirements.txt
└── README.md
```

## 📄 License

This project is licensed under the MIT License.


