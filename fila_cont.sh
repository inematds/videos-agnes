#!/bin/bash
cd /home/nmaldaner/projetos/videos-agnes
declare -A SLUG=( [wobbly2]="wobbly-robo-perdido" [luna2]="luna-segredo-do-oceano" [baloes2]="baloes-a-grande-tempestade" )
for h in wobbly2 luna2 baloes2; do
  echo "########## $h INICIO $(date +%H:%M) ##########"
  python3 -u rodar.py $h >> /home/nmaldaner/projetos/output/videos-agnes/$h.log 2>&1
  # move o filme final pro lives10 com nome limpo
  src="/home/nmaldaner/projetos/output/videos-agnes/$h/filme-$h.mp4"
  [ -f "$src" ] && cp "$src" "/home/nmaldaner/projetos/lives10/videos/${SLUG[$h]}.mp4" && echo ">> movido: ${SLUG[$h]}.mp4"
  echo "########## $h FIM $(date +%H:%M) ##########"
done
echo "TRES_CONTINUACOES_PRONTAS"
