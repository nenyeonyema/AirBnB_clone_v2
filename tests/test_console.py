#!/usr/bin/python3
"""
Unittests for console.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    @classmethod
    def setUpClass(cls):
        """Set up the class"""
        cls.console = HBNBCommand()

    def test_quit_command(self):
        """Test quit command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF_command(self):
        """Test EOF command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_emptyline(self):
        """Test emptyline method"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.emptyline()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_quit_command(self):
        """Test help quit command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help quit")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Exits the program with formatting")

    def test_help_EOF_command(self):
        """Test help EOF command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help EOF")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Exits the program without formatting")

    def test_noninteractive_mode_help(self):
        """Test non-interactive mode with help command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO('help\n')) as mock_stdin:
                self.console.cmdloop()
                output = mock_stdout.getvalue().strip()
                self.assertIn("(hbnb)", output)
                self.assertIn

    def test_create_command(self):
        """Test create command with new syntax"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel name=\"test name\" number_rooms=5")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Ensure output is not empty

 
    def test_create_command_invalid_syntax(self):
        """Test create command with invalid syntax"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel invalid_param=invalid_value")
            output = mock_stdout.getvalue().strip()
            self.assertIn("** attribute name missing **", output)

 

    def test_noninteractive_mode_quit(self):
        """Test non-interactive mode with quit command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO('quit\n')) as mock_stdin:
                self.console.cmdloop()
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "(hbnb)")


if __name__ == '__main__':
    unittest.main()
