#!/bin/bash
cd /home/nmaldaner/projetos/videos-agnes
for h in wobbly luna baloes; do
  echo "########## $h INICIO $(date +%H:%M) ##########"
  python3 -u rodar.py $h >> /home/nmaldaner/projetos/output/videos-agnes/$h.log 2>&1
  echo "########## $h FIM $(date +%H:%M) ##########"
done
echo "TRES_HISTORIAS_PRONTAS"
