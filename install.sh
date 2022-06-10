#!/bin/bash
echo "--------------------"
echo "|     Кто ты ?     |"
echo "|------------------|"
echo "| 1. Termux        |"
echo "| 2. Другой Unix   |"
echo "| 3. iSH           |"
echo "|                  |"
echo "| Введите 1/2/3:   |"
echo "--------------------"
read numb
if [ $numb = "1" ]
then
	pkg install python
	pkg install dos2unix
	pip install requests colorama proxyscrape
	cp ~/flowx/flowerx.py $PREFIX/bin/flowx
	dos2unix $PREFIX/bin/flowx
	chmod -R 777 ~/flowx
	chmod 777 $PREFIX/bin/flowx
	flowx
else
	if [ $numb = "2" ]
	then
		if [ "$(whoami)" != 'root' ];
		then
			echo "У вас нет прав. Запустите install.sh с root правами (sudo sh ~/spymer/install.sh)"
			exit
		else
			apt install python3 python3-pip dos2unix
			pip3 install requests colorama proxyscrape
			cp ~/flowx/flowerx.py $PREFIX/bin/flowx
			dos2unix $RPEFIX/bin/flowx
			chmod 777 $RPEFIX/bin/flowx
			chmod -R 777 ~/flowx
		    flowx
		fi
	else
		if [ $numb = "3" ] 
		then
			apk add python
			apk add python3
			apk add dos2unix
			pip3 install requests
			pip3 install colorama
			pip3 install proxyscrape
			cp ~/flowx/flowerx.py /usr/bin/flowx
			dos2unix /usr/bin/flowx
			chmod 777 /usr/bin/flowx
			flowx
		else
			echo "Некорректный ввод"
		fi
	fi
fi
