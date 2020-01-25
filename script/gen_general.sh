
python3 main.py --chars_file data/chars/vie_general.txt \
                --fonts_list data/fonts_list/vie.txt \
                --config_file configs/general.yaml \
                --bg_dir data/bg/ \
                --corpus_mode random \
                --length 150 \
                --num_img 200 \
                --img_height 96 \
                --tag randomize_general_1m_2 \
                --strict \
                --clip_max_chars \
                --num_processes 2
                # --debug \
                # --corpus_mode random \
                # --length 150 \
