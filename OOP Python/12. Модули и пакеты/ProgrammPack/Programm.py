from ProgrammPack.room import Room

class Programm:
    def __init__(self):
        print("Введите данные общих размеров комнаты в порядне Ширина - Длина - Высота: \n");
        self.room = Room(int(input()), int(input()), int(input()));
        self.interface();

    def interface(self):
        print("\n Меню \n \n Размеры комнаты: \n" + " Ширина - " + str(self.room.width) + " Длина - " + str(
            self.room.lenght) + " Высота - " + str(self.room.height));

        if (len(self.room.wd) > 0):
            i = 0;
            print("\n Отверстия в комнате:")
            for wd in self.room.wd:
                i += 1;
                print(' ' + str(i) + '.' + 'Ширина - ' + str(wd.width) + ' Высота - ' + str(wd.height));

        print(
            "\n Выберите действие которое хотите совершить: \n 1.Изменить размеры комнаты \n 2.Добавить отверстие \n 3.Удалить отверстие \n 4.Изменить размеры отверстия \n 5.Расчитать общею площадь комнаты \n 6.Расчитать рабочею площадь комнаты \n 7.Расчитать количество рулонов для покрытия \n 8.Закрыть программу");

        match input():
            case '1':
                self.room_size_edit();
            case '2':
                self.room_add_wd();
            case '3':
                self.room_wd_delete();
            case '4':
                self.room_wd_size_edit();
            case '5':
                print("\n Общея площадь комнаты: " + str(self.room.get_square()) + "\n");
                self.interface();
            case '6':
                print("\n Рабочая площадь комнаты: " + str(self.room.get_work_surface()) + "\n");
                self.interface();
            case '7':
                self.room_get_rolls();
            case '8':
                print("\n Спасибо, что использовали программу!");
            case _:
                print("\n Введен неверный пункт!");
                self.interface();

    def room_size_edit(self):
        print("\n Введите данные общих размеров комнаты в порядне Ширина - Длина - Высота: \n");
        self.room.width = input();
        self.room.lenght = input();
        self.room.height = input();

        print("\n Размеры комнаты успешно изменены! \n");
        self.interface();

    def room_add_wd(self):
        print("\n Введите данные размеров отверствия в порядке Ширина - Высота: \n");
        self.room.add_wd(int(input()), int(input()));

        print("\n Отверстие успешно добавлено! \n");
        self.interface();

    def room_wd_delete(self):
        if (len(self.room.wd) > 0):
            i = 0;
            print("\n Выберите отверстие которое хотите редактировать:");

            for wd in self.room.wd:
                i += 1;
                print(' ' + str(i) + '.' + 'Ширина - ' + str(wd.width) + ' Высота - ' + str(wd.height));

            check = int(input()) - 1;

            if (check <= len(self.room.wd) and check >= 0):
                self.room.wd.pop(check);

                print("\n Отверстие успешно удалено! \n");
                self.interface();

            else:
                print("\n Введен неверный номер!");
                self.room_wd_size_edit();
        else:
            print("\n Отверстия отсутствуют! \n");
            self.interface();

    def room_wd_size_edit(self):
        if (len(self.room.wd) > 0):
            i = 0;
            print("\n Выберите отверстие которое хотите редактировать:");

            for wd in self.room.wd:
                i += 1;
                print(' ' + str(i) + '.' + 'Ширина - ' + str(wd.width) + ' Высота - ' + str(wd.height));

            check = int(input()) - 1;

            if (check <= len(self.room.wd) and check >= 0):
                print("\n Введите данные размеров отверствия в порядке Ширина - Высота: \n");
                self.room.wd[check].width = int(input());
                self.room.wd[check].height = int(input());

                print("\n Размеры отверстия успешно изменены! \n");
                self.interface();

            else:
                print("\n Введен неверный номер!");
                self.room_wd_size_edit();
        else:
            print("\n Отверстия отсутствуют! \n");
            self.interface();

    def room_get_rolls(self):
        print("\n Введите данные размеров рулона в порядке Длина - Ширина: \n");
        roolsCount = self.room.get_number_of_rolls(int(input()), int(input()));
        print("\n Для покрытия комнаты потребуется " + str(roolsCount) + " рулонов \n");
        self.interface();
