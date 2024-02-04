# AutoAnnotation
Written in Python(Selenium) to Automate annotation with highly specialized Keyword
1. Downloading GeckoDriver:
Visit Mozilla's GeckoDriver GitHub Releases Page:
Go to the official releases page on GitHub to download the latest version of GeckoDriver. The URL is: GeckoDriver Releases

Download the Latest Release:
Find the latest release version and download the appropriate GeckoDriver executable for your operating system (Windows, Linux, or macOS). Ensure that you download the correct version based on your Firefox browser version.

Extract the Archive (if necessary):
If the downloaded file is a compressed archive (e.g., a zip file), extract its contents to a directory of your choice.

2. Configuring GeckoDriver:
Once you've downloaded GeckoDriver, you need to configure it for use with Selenium. Here's how:

Specify the Path in Your Script:
In your Python script, specify the correct path to the GeckoDriver executable. This is done in the following line:

python
Copy code
gecko_driver_path = "/bin/geckodriver"
Replace "/bin/geckodriver" with the actual path where you've placed the GeckoDriver executable.

Ensure Executability (Linux/macOS):
If you're using Linux or macOS, make sure that the GeckoDriver executable has the necessary permissions to be executed. You can use the chmod command to add execution permissions. For example:

bash
Copy code
chmod +x /path/to/geckodriver
Adjust System PATH (Optional):
Alternatively, you can add the directory containing GeckoDriver to your system's PATH environment variable. This allows you to specify just the executable name in your script without the full path.

Example of PATH Configuration (Linux/macOS):
bash
Copy code
# Open your shell profile file (e.g., .bashrc or .zshrc)
nano ~/.bashrc

# Add the following line to the end of the file, replacing "/path/to" with the actual path:
export PATH=$PATH:/path/to/directory/containing/geckodriver

# Save and exit the editor

# Restart your terminal or run the following command to apply the changes:
source ~/.bashrc
4. Running Your Script:
With GeckoDriver downloaded and configured, you should be able to run your Selenium script. Ensure that you have the necessary Python packages installed, such as Selenium:

bash
Copy code
pip install selenium
Then, execute your script, and it should automate interactions with the specified website using Firefox and GeckoDriver.

Remember to periodically check for updates to GeckoDriver to ensure compatibility with the latest versions of Firefox and Selenium.
