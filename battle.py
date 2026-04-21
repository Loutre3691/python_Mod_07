from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1, factory2):
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(f"{base1.describe()}\n  vs. \n{base2.describe()} \n  fight!")
    print(base1.attack())
    print(base2.attack())

if __name__ == "__main__":
    print("\033[1;36m"
          "              _,........__\n\
            ,-'            '`-.\n\
          ,'                   `-.\n\
        ,'                        \\\n\
      ,'                           .\n\
      .'\\               ,"".       `\n\
     ._.'|             / |  `       \\\n\
     |   |            `-.'  ||      `.\n\
     |   |            \033[1;36m'-._,'||      | \\\n\
     .`.,'   \033[1;31m ___ \033[0m     \033[1;36m`..,'.'      , |`-.\033[0m\n\
     \033[1;36ml       \033[1;31m/ _ \\ \033[0m\033[1;36m          ___ _/|`\n\
     \033[1;36m`-.._'-\033[0m\033[1;31m| |_| | \033[0m\033[1;36m _ _' -'\\`'\n\
\033[1;36m`.'''''-.`-..\033[0m\033[1;31m\\___/\033[0m\033[1;36m-----',' || .\n\
.'        `'-..___      __,'\\          \\  \\     \\\n\
\\_ .          |   `'''''    `.           . \\     \\\n\
  `.          |              `.          |  .     L\n\
    `.        |`--...________.'.        j   |     |\n\
      `._    .'      |          `.     .|   ,     |\n\
         `--,\\       .            `7''' |  ,      |\n\
            ` `      `            /     |  |      |    _,-''''`-.\n\
             \\ `.     .          /      |  '      |  ,'          `.\n\
              \\  v.__  .        '       .   \\    /| /              \\\n\
               \\/    `''\\'''''''''''''`.       \\   \\  /.''          |\n\
                `        .        `._ ___,j.  `/ .-       ,---.     |\n\
                ,`-.      \\         .'     `.  |/        j     `    |\n\
               /    `.     \\       /         \\ /         |     /    j\n\
              |       `-.   7-.._ .          |'          '         /\n\
              |          `./_    `|          |            .     _,'\n\
              `.           / `----|          |-............`---'\n\
                \\          \\      |          |\n\
               ,'           )     `.         |\n\
                7____,,..--'      /          |\n\
                                  `---.__,--.'\033[0m")
    print("\n\033[1;37m === Testing factory === \033[0m\n")
    test_factory(FlameFactory())
    print()
    print("\033[1;37m === Testing factory === \033[0m\n")
    test_factory(AquaFactory())
    print()
    print("\033[1;37m === Testing battle === \033[0m\n")
    test_battle(FlameFactory(), AquaFactory())
