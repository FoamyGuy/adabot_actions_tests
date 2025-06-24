import sys
import os


if len(sys.argv) > 1 and sys.argv[1] == "make_release":
    github_output_path = os.environ.get('GITHUB_OUTPUT')
    if github_output_path:
        with open(github_output_path, 'a') as f:
            f.write(f"release_created=true\n")

else:
    github_output_path = os.environ.get('GITHUB_OUTPUT')
    if github_output_path:
        with open(github_output_path, 'a') as f:
            f.write(f"release_created=false\n")


