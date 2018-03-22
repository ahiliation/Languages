if [ $1 == null ]
then
cat /dev/null > tmp.txt    
fi

if [ $1 == add ]
then
  cat tmp.txt >> sample1.txt
fi
