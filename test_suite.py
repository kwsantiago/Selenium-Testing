import unittest

# Import test-case files
from tc1_valid_input import TestValidInput
from tc2_empty_fields import TestEmptyFields
from tc3_invalid_email import TestInvalidEmail
from tc4_password_mismatch import TestPasswordMismatch

# Create a TestSuite object
test_suite = unittest.TestSuite()

# Add each test case to the suite
test_suite.addTest(unittest.makeSuite(TestValidInput))
test_suite.addTest(unittest.makeSuite(TestEmptyFields))
test_suite.addTest(unittest.makeSuite(TestInvalidEmail))
test_suite.addTest(unittest.makeSuite(TestPasswordMismatch))

# Run the test suite
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
