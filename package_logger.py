import subprocess
# This script fetches your homebrew Data,pip Data.
# Store pip packages in log
pip_packages = subprocess.check_output(['pip', 'list']).decode('utf-8')

# Store brew formulae and casks in log
brew_formulae = subprocess.check_output(['brew', 'list', '--formula']).decode('utf-8')
brew_casks = subprocess.check_output(['brew', 'list', '--cask']).decode('utf-8')

# Write log to file
with open('packages_log.txt', 'w') as f:
    f.write("Pip Packages:\n")
    f.write(pip_packages)
    f.write("\nBrew Formulae:\n")
    f.write(brew_formulae)
    f.write("\nBrew Casks:\n")
    f.write(brew_casks)
