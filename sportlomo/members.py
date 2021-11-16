import sportlomo


def main():
    members = sportlomo.get_members()
    print(members)
    print(len(members))


if __name__ == "__main__":
    main()
