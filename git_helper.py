import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_git_command(command, cwd=None):
    """Run a git command and return the output"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        
        if result.returncode != 0:
            return False, result.stderr
        return True, result.stdout
    except Exception as e:
        return False, str(e)

def main():
    # Create root window and hide it (just used for dialogs)
    root = tk.Tk()
    root.withdraw()
    
    # Ask user to browse for the Git repository
    repo_path = filedialog.askdirectory(title="Select Git Repository")
    if not repo_path:
        messagebox.showinfo("Cancelled", "No directory selected.")
        return
    
    # Check if it's a Git repository
    success, output = run_git_command("git status", cwd=repo_path)
    if not success:
        messagebox.showerror("Error", f"This is not a Git repository or Git is not installed.\n{output}")
        return
    
    # Add all files
    success, output = run_git_command("git add -A", cwd=repo_path)
    if not success:
        messagebox.showerror("Error", f"Failed to add files:\n{output}")
        return
    
    # Use fixed commit message instead of asking
    commit_message = "new commit"
    
    # Commit changes
    success, output = run_git_command(f'git commit -m "{commit_message}"', cwd=repo_path)
    if not success:
        messagebox.showerror("Error", f"Failed to commit:\n{output}")
        return
    
    # Get current branch
    success, branch = run_git_command("git rev-parse --abbrev-ref HEAD", cwd=repo_path)
    if not success:
        messagebox.showerror("Error", f"Failed to determine current branch:\n{branch}")
        return
    
    branch = branch.strip()
    
    # Push changes
    success, output = run_git_command(f"git push origin {branch}", cwd=repo_path)
    if not success:
        messagebox.showerror("Error", f"Failed to push to remote:\n{output}")
        return
    
    messagebox.showinfo("Success", "Successfully committed and pushed all changes!")
    root.destroy()

if __name__ == "__main__":
    main() 