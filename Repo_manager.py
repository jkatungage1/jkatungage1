import sys, os, subprocess, time, git, shutil; from pathlib import Path
from git import Repo
PROJECT_DIR = os.path.normcase(Path(__file__).parent)

def git_pull(*args) :
    # print('Running git pull...')
    if "S" in args:
        print("Using Subprocess module")
        # USING SUBPROCESS MODULE
        try :
            command = subprocess.run(["git", "status"], cwd=PROJECT_DIR, check=True)
            print('Git status complete.')
            assert True
            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    if "O" in args:
        print("Using OS module")
        # USING OS MODULE
        try :
            command = os.system(f"cd {PROJECT_DIR} && git status")
            assert True
            print('Git status complete.')
            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    else:
        # USING git MODULE
        print("Using git module")
        try :
            deployment_repo = Repo(PROJECT_DIR)
            assert not deployment_repo.bare
            master = deployment_repo.heads.master
            log = master.log()
            print(log[0])

            git_cmd = deployment_repo.git
            if not git_cmd.checkout("master").returncode == 0:
                git_cmd.stash()

            assert git_cmd.pull("origin","master")
            # time.sleep(5)

        except git.exc.GitCommandError as e:
            print(f"Git Command Error: {e}")

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

def git_commit(repo_name:str, *args):
    # print('Running git pull...')

    if "S" in args:
        print("Using Subprocess module")
        # USING SUBPROCESS MODULE
        try :
            command = subprocess.run(["git", "add" , "-u"], cwd=f"{PROJECT_DIR}\{repo_name}", check=True)
            commit_message = input("Enter commit message: ")
            command = subprocess.run(["git", "commit", "-m", commit_message], cwd=f"{PROJECT_DIR}\{repo_name}", check=True)
            assert command.returncode == 0
            print('Git commit complete.')
            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    if "O" in args:
        print("Using OS module")
        # USING OS MODULE
        try :
            command = os.system(f"cd {PROJECT_DIR} && git add -u")
            commit_message = input("Enter commit message: ")
            command = os.system(f'cd {PROJECT_DIR} && git commit -m "{commit_message}"')
            assert command == 0
            print('Git status complete.')
            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    else:
        # USING git MODULE
        print("Using git module")
        try :
            deployment_repo = Repo(PROJECT_DIR)
            assert not deployment_repo.bare
            master = deployment_repo.heads.master
            # git_pull()
            log = master.log()
            print(log[0])

            git_cmd = deployment_repo.git
            # if not git_cmd.checkout("master"):
            #     None# git_cmd.checkout("master",b="Test")
            if "nothing" in git_cmd.status() :
                print("No changes to commit")
                exit(0)
            else :
                commit_message = input("Enter commit message: ")
                assert git_cmd.add("-u") == ''
                assert git_cmd.commit("-m", f"{commit_message}") != ''


        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error: {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

def git_clone(*args) -> str:
    # print('Running git pull...')
    if "S" in args:
        print("Using Subprocess module")
        # USING SUBPROCESS MODULE
        try :
            repo_url = input("Enter repository url: ")
            repo_name = repo_url.split('/')[-1].split('.')[0]
            destination_folder = input("Enter destination folder(absolute path): ")
            destination_folder = os.path.normcase(destination_folder)
            command = subprocess.run(["git", "clone", f'{repo_url}'], cwd=destination_folder,check=True)
            assert command.returncode == 0
            print('Git clone complete.')
            input("Press Enter to continue...")

            # command = os.system(f'RMDIR /S "{destination_folder}\\{repo_name}"')

            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            # exit(0)

    if "O" in args:
        print("Using OS module")
        # USING OS MODULE
        try :
            command = os.system(f"cd {PROJECT_DIR} && git add -u")
            commit_message = input("Enter commit message: ")
            command = os.system(f'cd {PROJECT_DIR} && git commit -m "{commit_message}"')
            assert command == 0
            print('Git status complete.')
            # time.sleep(5)

        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    else:
        # USING git MODULE
        print("Using git module")
        try :
            deployment_repo = Repo(PROJECT_DIR)
            assert not deployment_repo.bare
            master = deployment_repo.heads.master
            # git_pull()
            log = master.log()
            print(log[0])

            git_cmd = deployment_repo.git
            # if not git_cmd.checkout("master"):
            #     None# git_cmd.checkout("master",b="Test")
            if "nothing" in git_cmd.status() :
                print("No changes to commit")
                exit(0)
            else :
                commit_message = input("Enter commit message: ")
                assert git_cmd.add("-u") == ''
                assert git_cmd.commit("-m", f"{commit_message}") != ''


        except AssertionError as e:
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

    return repo_name


def main(*args:str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fr"{PROJECT_DIR}")
    args = list(args)
    for car in args:
        args[args.index(car)] = car.upper()

    repo_name = git_clone(*args)
    print(f"Repo name: {repo_name}")
    os.system(fr'echo "Bonjour" > "{PROJECT_DIR}\deplo\{repo_name}\bonjour.txt"')
    git_commit(repo_name=repo_name,*args)
    # git_pull(*args)


if __name__ == '__main__':
    os.system(f'cd {PROJECT_DIR}')
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
            time.sleep(2)
    else: print("No arguments provided.")
    try :
        main("s")
        # main(sys.argv[1] if len(sys.argv) > 1
        #     else sys.argv[1],sys.argv[2] if len(sys.argv) > 2 else "")
    except Exception as e:
        print(f"Error: {e}")


