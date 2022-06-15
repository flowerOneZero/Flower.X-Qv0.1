#!/bin/bash
echo "---------------------------------"
echo "|     Выберите действие         |"
echo "|-------------------------------|"
echo "| 1. ЗАПУСК СКРИПТА             |"
echo "| 2. ОБНОВИТЬ СКРИПТ            |"
echo "|                               |"
echo "| Введите 1/2                   |"
echo "---------------------------------"
read numb
if [[ $numb = '2' ]]; then
    echo "Вы уверены?(y/n)"
    read otvet
    if [[ $otvet = 'y' ]]; then 
        cd && rm -rf Flower.X-Qv0.1 && git clone https://github.com/flowerOneZero/Flower.X-Qv0.1.git && cd Flower.X-Qv0.1 && ./setup.sh
    fi
else
    echo "---------------------------------"
    echo "|     Выберите вашу систему     |"
    echo "|-------------------------------|"
    echo "| 1. Termux                     |"
    echo "| 2. Ubuntu/mint/Debian/Kali    |"
    echo "| 3. Arch/Manjaro               |"
    echo "|                               |"
    echo "| Введите 1/2/3:                |"
    echo "---------------------------------"
    read numb
    case $numb in
        1)
            echo "Установка neofetch"
            pkg install neofetch;;
        2)
            echo "Установка neofetch"
            sudo apt install neofetch;;
        3)
            echo "Установка neofetch"
            sudo pacman -S neofetch;;
        *)
            echo "Скрипт выполнен не будет. Проверьте вводимое число.";;
    esac
    pip install requirements.txt
    python flowerx.py
fi