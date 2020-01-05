python3 main.py --chars_file data/chars/vie.txt \
                --fonts_list data/fonts_list/vie.txt \
                --config_file configs/vbpl.yaml \
                --bg_dir data/bg/ \
                --corpus_mode vbpl \
                --length 150 \
                --num_img 50 \
                --img_height 96 \
                --tag randomize_400k \
                --strict \
                --clip_max_chars \
                --num_processes 2
                # --debug \
                # --corpus_mode random \
                # --length 150 \
