echo "--- evaluate knnjoin ---"
nvprof --kernels KNNQuery_base --metrics all ./knnjoin 145057 145057 4 800 800 200 Skin_NonSkin.txt Skin_NonSkin.txt &>metrics.txt
echo "--- evaluate knnjoin_opt ---"
nvprof --kernels KNNQuery_base --metrics all ./knnjoin_opt 145057 145057 4 800 800 200 Skin_NonSkin.txt Skin_NonSkin.txt &>metrics_opt.txt
