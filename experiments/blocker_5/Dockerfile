FROM aflplusplus/aflplusplus:latest

# ── Source ────────────────────────────────────────────────────────────────────
WORKDIR /experiment
COPY targets/blocker_5/blocker_5.c ./blocker_5.c
COPY experiments/blocker_5/run.sh  ./run.sh
RUN chmod +x run.sh

# ── Output volume (queues + summary land here) ────────────────────────────────
VOLUME /output

CMD ["./run.sh"]
