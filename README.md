# PronouncUR

This tool generates a pronunciation dictionary from a list of Urdu words in a form, suitable for use with a speech recognizer, such as [CMUSphinx](https://cmusphinx.github.io/), [KALDI](http://kaldi-asr.org/) and text-to-speech system, such as [MaryTTS](http://mary.dfki.de/).

Read my lips - this tool works only for Urdu. This means this tool only support Urdu graphemes (letters).

# Requirement(s)

This tool requires [TensorFlow](https://www.tensorflow.org/) and [Sequence-to-Sequence G2P toolkit](https://github.com/cmusphinx/g2p-seq2seq). Please see [requirements.txt](https://github.com/harisbinzia/PronouncUR/blob/master/requirements.txt) for details.

# Model

A pretrained model (2-layer LSTM with 512 hidden units) is [available for download](https://github.com/harisbinzia/PronouncUR/tree/master/itudict). The model is trained on a handcrafted expert lexicon of around 39,000 words.

# Reference(s)

If you use this tool in any of your work, please cite below paper.

[PronouncUR: An Urdu Pronunciation Lexicon Generator](http://www.lrec-conf.org/proceedings/lrec2018/pdf/646.pdf)

```
@InProceedings{BIN ZIA18.646,
  author = {Haris Bin Zia ,Agha Ali Raza and Awais Athar},
  title = {PronouncUR: An Urdu Pronunciation Lexicon Generator},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year = {2018},
  month = {may},
  date = {7-12},
  location = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {979-10-95546-00-9},
  language = {english}
  }
```

# License

See the [LICENSE](https://github.com/harisbinzia/PronouncUR/blob/master/LICENSE) file.
