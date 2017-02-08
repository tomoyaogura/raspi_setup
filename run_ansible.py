import re
import inquirer
import subprocess

HOSTS_DIR = "hosts"
MAIN_YML_DIR = "roles/common/tasks/main.yml"
PATTERN_COMMENT = "\n#(?:\s*)- include: (.*)"
PATTERN_RUN = "\n- include: (.*)"
PATTERN_ANY = "include: (.*)"

PATTERN_EDIT_COMMENT = "#(?:\s*) - include: "
PATTERN_RUN_COMMENT = "- include: "
PATTERN_REPLACE_COMMENT = "# - include: "

def read_main_yml():
    f = open(MAIN_YML_DIR)
    txt = f.read()
    commented_matches = re.finditer(PATTERN_COMMENT, txt)
    run_matches = re.finditer(PATTERN_RUN, txt)
    commented = [match.group(1) for match in commented_matches]
    run = [match.group(1) for match in run_matches]
    f.close()
    return (run, commented)

def read_hosts_yml():
    f = open(HOSTS_DIR)
    return f.readlines()[1:]

def run_script():
    subprocess.call("ansible-playbook deploy.yml --private-key=\
            ~/.ssh/raspi_1/raspi_1_id_rsa -K -u pi -i hosts")
    return

def edit(line, comment, run):
    word = re.finditer(PATTERN_ANY, line)[0].group(1)
    if word in comment:
        return re.sub("# -", "-", line)
    elif word in run:
        return re.sub("^-", "# -", line)
    else:
        return line


def replace_main_yml(comment, run):
    f = open(MAIN_YML_DIR)
    lines = f.readlines()
    edited_lines = [edit(line, comment, run) for line in lines]

if __name__=="__main__":
    # Read files to print to confirm run
    run, commented = read_main_yml()
    hosts = read_hosts_yml()
    print("Will run the following roles:")
    for r in run:
        print(r)
    print("\nOn the following hosts:")
    for h in hosts:
        print(h)

    questions = [
        inquirer.Confirm('continue', message="Do you want to change roles")
    ]
    answer = inquirer.prompt(questions)

    if(answer['continue']):
        # run_script()
        print("Ran script")
    else:
        # Take comment to decide which roles to run
        questions = [
            inquirer.Checkbox('roles',
                              message="What roles do you want to install",
                              choices=run+commented)
        ]
        answers = inquirer.prompt(questions)['roles']
        print answers
        remove = [i for i in run+commented if i not in answers]
        print remove
        #comment_out(remove)
        #uncomment(answers)




