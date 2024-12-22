# Password Complexity Checker

## Overview
The Password Complexity Checker is designed to evaluate the strength of user-provided passwords based on various criteria. This tool provides users with immediate feedback, helping them to create more secure passwords that meet modern security standards.

## Features
- **Length Assessment**: Checks if the password meets a minimum length requirement.
- **Character Diversity**:
  - Evaluates the presence of uppercase and lowercase letters.
  - Detects numbers.
  - Identifies special characters.
- **Strength Feedback**:
  - Ranges from "Weak" to "Very Strong" based on password complexity.
  - Provides actionable suggestions for improvement.
- **Real-Time Validation**: Offers instant results as the user types (if integrated into a front-end application).

## Technologies Used
- **Programming Language**: Python
- **Additional Libraries**:
  - `re` for regular expressions
  - `argparse` for CLI implementations (optional)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/G0wda/Password_complexity_checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Password_complexity_checker
   ```
3. Install dependencies (if required):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### CLI
1. Run the tool in your terminal:
   ```bash
   python Password_complexity_checker.py
   ```
2. Enter your password when prompted to receive an assessment.

### Integration
You can integrate this tool into larger applications by importing the main assessment function:
```python
from Password_complexity_checker import assess_password_strength

feedback = assess_password_strength("YourPassword123!")
print(feedback)
```



## Password Strength Criteria
| Strength       | Requirements                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Weak           | Fewer than 8 characters or only one type of character (e.g., all lowercase) |
| Moderate       | At least 8 characters, including two character types                        |
| Strong         | At least 12 characters, including three character types                     |
| Very Strong    | 16+ characters, including all four character types                          |

## Example Output
### Input
```
Password: Password123!
```
### Feedback
```
Strength: Strong
Suggestions: Consider adding more unique characters for additional security.
```

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or feedback, please contact santhoshgowda9542@gmail.com or open an issue in the repository.
