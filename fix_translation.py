import re

file_path = r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern 1
p1 = r'위에서 보듯이, 트랜스포머 어텐션 계층\(Attention Layer\)은 여러 개의 완전히 독립적인 어텐션 헤드로 생각한다(.*?)이 두 장치는 완전히 병렬로 작동하며 각각 출력을 잔차 스트림\(Residual Stream\)에 다시 추가합니다\. 하지만 트랜스포머 층이 일반적으로 이렇게 제시되는 것은 아니며, 이들이 동등하다는 것이 명확하지 않을 수도 있습니다\.'
r1 = r'위에서 살펴보았듯이, 트랜스포머 어텐션 계층(Attention Layer)은 여러 개의 완전히 독립적인 어텐션 헤드\1로 구성되어 있다고 생각할 수 있습니다. 이들은 완전히 병렬로 작동하며, 각각의 출력을 잔차 스트림(Residual Stream)에 더해줍니다. 하지만 트랜스포머 계층이 일반적으로 이런 방식으로 설명되지는 않으므로, 이 두 관점이 서로 수학적으로 동등하다는 사실이 직관적으로 다가오지 않을 수도 있습니다.'
text = re.sub(p1, r1, text, flags=re.DOTALL)

# Pattern 2: Vaswani
p2 = r'원래의 바스와니에서 <span style="font-style:italic">등\.</span>&nbsp;트랜스포머에 관한 논문 (.*?)어텐션 계층\(Attention Layer\)의 출력은 결과 벡터를 중첩하여 설명한다(.*?), 그리고 출력 행렬로 곱한 것이다\.(.*?)\. 우리 흩어지자(.*?)각 헤드마다 동일한 크기의 블록으로 나눠(.*?)\. 그다음 다음을 관찰합니다:'
r2 = r'Vaswani 등이 발표한 기념비적인 트랜스포머 논문 \1 에서는 어텐션 계층(Attention Layer)의 출력을 결과 벡터 \2 를 연결(concatenate)한 뒤 출력 행렬 \3 를 곱하는 방식으로 설명합니다. 이제 \4 를 각 헤드에 대응하는 동일한 크기의 블록 \5 으로 나누어 봅시다. 그러면 다음과 같은 식을 도출할 수 있습니다:'
text = re.sub(p2, r2, text, flags=re.DOTALL)

# Pattern 3
p3 = r'이는 각각의 출력 행렬을 곱하여 잔차 스트림\(Residual Stream\)에 더하는 독립적인 헤드와 동등하다는 것을 드러낸다\. 연결 정의는 더 크고 계산 효율적인 행렬 곱셈을 생성하기 때문에 종종 선호됩니다\. 하지만 이론적으로 트랜스포머를 이해하기 위해서는 독립적인 가산으로 생각하는 것을 선호합니다\.'
r3 = r'이는 각 헤드가 독립적으로 자신의 출력 행렬을 곱한 뒤 잔차 스트림(Residual Stream)에 그 결과를 더하는 것과 완전히 동일함을 보여줍니다. 연결(concatenation)을 이용한 정의는 더 크고 계산 효율성이 높은 행렬 곱셈을 만들어내기 때문에 실제 구현에서 종종 선호됩니다. 하지만 트랜스포머를 이론적으로 이해할 때는, 각 어텐션 헤드가 독립적이며 그 결과가 덧셈을 통해 결합(additive)된다고 생각하는 것이 더 바람직합니다.'
text = re.sub(p3, r3, text, flags=re.DOTALL)

# Pattern 4
p4 = r'하지만 주의 중심이 독립적으로 행동한다면, 그들은 무엇을 할까요\? 어텐션 헤드의 근본적인 행동은 정보를 이동시키는 것입니다\.&nbsp;한 토큰의 잔차 스트림\(Residual Stream\)에서 정보를 읽어 다른 토큰의 잔차 스트림\(Residual Stream\)에 씁니다\. 이 절에서 얻을 주요 관찰점은, 어떤 토큰에서 정보를 이동시키는지와 어떤 정보가 \'읽히는\' 것과 목적지에 어떻게 \'쓰인지\' 완전히 분리된다는 점입니다\.'
r4 = r'어텐션 헤드가 이처럼 독립적으로 작동한다면, 이들은 정확히 어떤 역할을 할까요? 어텐션 헤드의 근본적인 역할은 바로 정보를 이동(move)시키는 것입니다.&nbsp;한 토큰의 잔차 스트림(Residual Stream)에서 정보를 읽어(read), 다른 토큰의 잔차 스트림에 정보를 쓰는(write) 역할을 합니다. 이번 장에서 주목해야 할 핵심은, \'어느 토큰에서\' 정보를 이동시킬지 결정하는 과정이, \'어떤 정보\'를 읽어 목적지에 \'어떻게 쓸지\' 결정하는 과정과 완벽하게 분리(separable)되어 있다는 사실입니다.'
text = re.sub(p4, r4, text, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement complete.")
