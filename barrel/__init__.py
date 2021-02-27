# run when module is imported
# ("python -m barrel")
# ("python barrel/__init__.py")
print("__init__:base")

if __name__ == "__main__":
    print("__init__:__name__==__main__")
    