# Milestone 2 “Secret messages”
Alice and Bob are bored during their classes and they want to exchange messages for fun. To avoid the situation when the teachers catch them and read their notes, they agreed to encrypt their messages using the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

To make it more secure, they will use a new key every day, so they need help to automatically encrypt and decrypt messages. They ask for your help.

Create two Python files `encrypt.py` and `decrypt.py`, which will read the user message and the key and will output the results.

For example:

```bash
python encrypt.py
Enter key: 1
Enter message: The quick brown fox jumps over the lazy dog.

Result: Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.

###

python decrypt.py
Enter key: 1
```
> [!NOTE] only letters get shifted with the preservation of case (e.g., `T->U` and `t->u`), while punctuation symbols stay the same.