import sys, os, subprocess, time, git; from pathlib import Path
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

def git_commit(*args):
    # print('Running git pull...')
    if "S" in args:
        print("Using Subprocess module")
        # USING SUBPROCESS MODULE
        try :
            command = subprocess.run(["git", "add" , "-u"], cwd=PROJECT_DIR, check=True)
            commit_message = input("Enter commit message: ")
            command = subprocess.run(["git", "commit", "-m", commit_message], cwd=PROJECT_DIR, check=True)
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
            print("Unknown Assertion Error" if str(e) == "" else f"Assertion Error : {e}")
            exit(1)

        except Exception as e:
            print(f"Error: {e}" if "git" in str(e) else "Uknonwn error")
            exit(1)

        finally:
            print("Finally block executed.")
            exit(0)

def main(*args:str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fr"{PROJECT_DIR}")
    args = list(args)
    for car in args:
        args[args.index(car)] = car.upper()

    git_commit(*args)
    git_pull(*args)


if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
        time.sleep(10)
    else: print("No arguments provided.")
    a = [s for s in sys.argv[1:]]
    
    main()
    
