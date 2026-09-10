---
title: "Selected Excerpts - Section 4.2"
source: html/excerpts1.html
---

[ [preface](pages/excerpts0.md) | [section 4.2](pages/excerpts1.md) | [section 10.0](pages/excerpts2.md) | [section 18.0](pages/excerpts3.md) | [section 22.0](pages/excerpts4.md) ]

## Section 4.2

# Incompleteness versus Incomputability

While Turing's result on incomputability is concerned with the limitations of computers and Gödel's result is concerned with the limitation of mathematics, Turing's result is more general in that Gödel's result is a special case of it. This is because the notion of proof verification can be automated by a computer since any of the mathematical statements from the previous section can be implemented as programs. Therefore, asking the question “Is there a proof for a mathematical statement?” can always be reexpressed as “Does some program halt?”

Despite this fact, from a purely subjective and intuitive point of view, Gödel's theorem seems to be more profound because it is primarily concerned with the limitations of mathematics and, by implication, the limitations of mathematicians as well as other humans. On the other hand, some mathematicians, most notably Roger Penrose in his best-selling book *The Emperor's New Mind*, have taken Gödel's incompleteness result to be evidence that human minds do something that no computer could ever do. To paraphrase, the argument works something like this:

>  Looking at Gödel's statement, we know that it must undoubtedly be true, since if it is false, we reach a contradiction. You and I, being humans, were able to “leap” out of the formal mathematics to see the validity of Gödel's statement. This ability to see beyond mathematics demonstrates that in some ways, human thought is not only non-algorithmic, but also intrinsically more powerful than algorithmic processes.

Many scientists, philosophers, and mathematicians have pointed out that there are at least two problems with Penrose's interpretation of Gödel's incompleteness result. First, while Gödel's incompleteness result certainly implies that there are true mathematical statements that cannot be proven true---with [ Gödel's Statement ] being just one example---it does not necessarily follow that a computer cannot “see” the validity of a Gödel statement with any less certainty than we could. Why? Because, within predicate calculus, neither you nor I (nor anyone else) would be able to prove a Gödel statement. “Seeing” truth is not the same as proving truth. Nevertheless, Gödel did prove that the Gödel statement was true, *but not in predicate calculus*. His proof was in a formal system of mathematics that was slightly more powerful than the system he started out with. Let's denote the original system, predicate calculus, by the symbol ***P***, and the system in which Gödel proved his incompleteness result by the symbol ***P'***. Is ***P'*** immune to Gödel's incompleteness? Surprisingly, ***P'*** is also incomplete. We can prove this by using another formal system, ***P”***, which is also incomplete (but provably so in ***P”'***), and so on.

The second problem with the argument is that Penrose assumes that humans are both complete and consistent. If humans were somehow immune to Gödel's incompleteness, then (as computational systems) we would have to be either inconsistent or so computationally weak that self-referential statements could not be expressed. Either of these results would imply that humans are, at least in some ways, weaker than computers. But even if humans are consistent, we aren't immune to Gödel's incompleteness. This is illustrated by the following humorous scenario, which I quote, with some minor editing, from Peter Grogono [1]:

>  Imagine that we have an instrument with which we can examine Penrose's brain in great detail (a sort of souped-up interactive NMR scanner, perhaps). After some investigation, we find a neuron, ***G***, with the following property: ***G*** is usually dormant, but if we tell Penrose that ***G*** is dormant, ***G*** promptly fires. Then there is a true fact (***G*** is dormant) that Penrose can never know because, whenever he knows it, it is false. Furthermore, we can know this because we are “outside the system.”

It is unlikely that a neuron with this property exists. It is very likely, however, that there are some aspects of Penrose's brain's behavior that he cannot know, because knowing them would render them false. Thus Penrose is not exempt from Gödel's theorem.

Furthermore, consider the sentence “Penrose cannot truthfully assert this statement.” You and I can say this sentence without contradicting ourselves. But no matter how Penrose contorts himself, he cannot say the sentence without being inconsistent. Moreover, Penrose can “see” the validity of the statement, but he is helpless to express it truthfully, unlike us, because we are “outside” of the system that is Penrose.

---

[1]   From a posting on the USENET newsgroup `comp.ai.alife`, dated September 29, 1995.

[ [preface](pages/excerpts0.md) | [section 4.2](pages/excerpts1.md) | [section 10.0](pages/excerpts2.md) | [section 18.0](pages/excerpts3.md) | [section 22.0](pages/excerpts4.md) ]
