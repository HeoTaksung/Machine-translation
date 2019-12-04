# 기계 번역 평가를 위한 2가지 알고리즘 BLEU, METEOR
## 1. BLEU (BiLingual Evaluation Understudy)

* BLEU 평가의 기본 단위는 문장이다.  
  
* 품질은 기계(후보)에서 출력된 텍스트와 사람(참조)이 직접 작성한 텍스트 사이의 얼마나 유사한가를 따진다.  
  
* 기계 번역이 사람과의 번역과 가까우면 가까울수록 좋다.  
  
* 즉, 이는 BLEU의 값이 크면 클수록 더 일치한다는 것이다.
    
* BLEU의 값은 0~1사이의 숫자이며 n-gram을 통한 순서쌍들이 겹치는 개수와 후보 단어수, 참조 단어수에 따라 값이 바뀐다.
    
* BLEU 디렉토리에 있는 코드는 unigram ~ quadrigram까지 측정하는 코드이다.  

**Wikipedia Link: [BLEU](https://en.wikipedia.org/wiki/BLEU)**  
**BLEU Paper Link: [BLEU_Paper](https://www.aclweb.org/anthology/P02-1040.pdf)**

----------------------------------------------
## 2. METEOR (Metric for Evaluation of Translation with Explicit ORdering)
    
* METEOR는 BLEU와 마찬가지로 평가의 기본 단위는 문장이다.
    
* 이는 BLEU에서의 단점을 수정하기 위한 알고리즘 BLEU보다 좋은 상관 관계가 나타난다.
    
* 측정 기준은 unigram 정밀도 및 리콜의 고조파 평균을 기반으로 하며 정확도보다 가중치가 높은 리콜을 사용한다.
    
* METEOR의 값 또한 0~1사이의 숫자이며 unigram수, 후보 단어수, 참조 단어수, chunk 수에 따라 값이 바뀐다.
    
* 여기서 chunk 수는 unigram으로 가장 적은 chunk로 그룹화되며, 참조와 후보 문장에 인접하지 않은 매핑이 많을수록 penalty가 높아진다.

**Wikipedia Link: [METEOR](https://en.wikipedia.org/wiki/METEOR)**  
**METEOR Paper Link: [METEOR_Paper](https://www.cs.cmu.edu/~alavie/papers/BanerjeeLavie2005-final.pdf)**
