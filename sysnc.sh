## ��ȡ����

sleep 1

git add .
echo "input the message you wanna commit:"
read message
git commit -m "$message" --no-verify
echo "start to pull����"
git pull origin master

pid=$!

wait ${pid}

##�ύ����

echo "start to push����"
git push origin master

pid=$!

wait ${pid}

echo "Close in 5s"
sleep 1
echo "Close in 4s"
sleep 1
echo "Close in 3s"
sleep 1
echo "Close in 2s"
sleep 1
echo "Close in 1s"
sleep 1