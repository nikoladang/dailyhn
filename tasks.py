from invoke import run, task

@task
def build(clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")

@task
def hi(name):
    print("Hi {0}!".format(name))
