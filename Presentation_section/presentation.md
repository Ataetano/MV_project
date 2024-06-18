---

marp: true
theme: gaia
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  .author-list {
    line-height: 0.4;
  }
  .container {
    display: flex;
    justify-content: space-between;
  }
  .column {
    flex: 1;
    padding: 0 10px;
  }
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
  svg[id^="mermaid-"] { 
    min-width: 550px; 
    max-width: 960px; 
    min-height: 400px; 
    max-height: 500px;
  }



---

<img src="img/conference_logo.jpg" width="15%" />

#### Generating Music Variations through Chaotic Dynamical Systems Exploration

###### Rajamangala University of Technology Thanyaburi
<img style="float: right;" src="img/qrcode.png" width="20.5%" />
<div class="author-list">
  <p>Wannasa Rianthong</p>
  <p>Kanatsanun Sub-udom</p>
  <p>Patipan Somwong</p>
</div>

---

#### Nowaday Music AI 

###### Example of Music AI 

<br>

<div class="container">
  <div class="column">
    <center>
    <img src="img/mubert.jpg" width="91%" />
    </center>
  </div>
  <div class="column">
    <center>
    <img src="img/aiva.png" width="50%" />
    </center>
  </div>
  <div class="column">
    <center>
    <img src="img/sounddraw.jpg" width="90%" />
    </center>
  </div>
</div>

###### Pros and Cons of Music AI 

<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 1px solid black;">
      <th style="padding: 10px;"><h5>Pros</h5></th>
      <th style="padding: 10px;"><h5>Cons</h5></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px; border-bottom: 0px; background-color: transparent;"><h6>user friendly</h6></td>
      <td style="padding: 10px; border-bottom: 0px; background-color: transparent;"><h6>high resource</h6></td>
    </tr>
    <tr>
      <td style="padding: 10px; border-bottom: 1px solid black; border-top: 0px;"><h6>support various style</h6></td>
      <td style="padding: 10px; border-bottom: 1px solid black; border-top: 0px;"><h6>unrepeatable</h6></td>
    </tr>
  </tbody>
</table>

---

![bg left:50% fit](img/dp.png) 
> D. S. Dabby (1996), Musical Variations from a Chaotic Mapping, Chaos, 6 (2): pp. 95–107. 

![center h:250px ](img/le.png)
![center h:100px](img/music.png)

---

##### MVCM 1. Find a sequence of music pitches (SMP)
<br>
<center>
  <h6>Original</h6>
  <br>
  <img src="img/dp_1.png" width="100%" />
  <img src="img/dabby_1.png" width="75%" />
  <br>
  <audio controls>
    <source src="mp3/dabby_1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

---

##### MVCM 2. Determine a trajectory (TRAJ)

$$
\begin{aligned}
\dot{x}_1 &= 10(x_2 - x_1) \\
\dot{x}_2 &= 28x_1 - x_2 - x_1x_3 \\
\dot{x}_3 &= x_1x_2 - 2.67x_3
\end{aligned}
\implies
\boxed{\begin{array}[c]
\text{RK4} \\
x_1(0) = x_2(0) = x_3(0) = 1.00 \\
h = 0.01
\end{array}}
$$

|       | $t = 0$ | $t = h$ | $t = 2h$ | $t = 3h$ | $t = 4h$ | $\dots$ | $t = 9h$ | $t =  10h$ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| $k$ | 0 | 1 | 2 | 3 | 4 | $\dots$ | 9 | 10 |
| $x_1$ | 1.00 | 1.29 | 2.13 | 3.74 | 6.54 | $\dots$ | 7.55 | 1.20 | 
| $x_2$ | 1.00 | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| $x_3$ | 1.00 | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |

----- 

#### MVCM 3. Construct a mapping: SMP vs TRAJ

<br>
<center>
  <section data-marpit-fragments="1">
  <img src="img/dp_1.png" width="100%" />
  <br>
  <br>
  <img src="img/dp_2.png" width="100%" />
  <br>
  <br>
  <img data-marpit-fragment="1" src="img/dp_3.png" width="100%" />
  </section>
</center>

---

#### MVCM 4. Alternate the initial condition

$$
\begin{aligned}
\dot{x}_1 &= 10(x_2 - x_1) \\
\dot{x}_2 &= 28x_1 - x_2 - x_1x_3 \\
\dot{x}_3 &= x_1x_2 - 2.67x_3
\end{aligned}
\implies
\boxed{\begin{array}[c]
\text{RK4} \\
{\color{blue}x_1(0) = 1.01}, x_2(0) = x_3(0) = 1.00 \\
h = 0.01
\end{array}}
$$

|       | $t = 0$ | $t = h$ | $t = 2h$ | $t = 3h$ | $t = 4h$ | $\dots$ | $t = 9h$ | $t =  10h$ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| $k$ | 0 | 1 | 2 | 3 | 4 | $\dots$ | 9 | 10 |
| $x_1$ | 1.01 | 1.30 | 2.15 | 3.76 | 6.58 | $\dots$ | 7.48| 1.15 | 
| $x_2$ | 1.00 | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| $x_3$ | 1.00 | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ | $\dots$ |

----- 

#### MVCM 5. Construct the sequence of new music pitch

<br>
<center>
  <img src="img/dp_3.png" width="100%" />
  <br>
  <br>
  <img src="img/dp_4.png" width="100%" />
  <br>
  <br>
</center>

---

#### MVCM 5. Construct the sequence of new music pitch
<br>
<center>
  <img src="img/dp_3.png" width="100%" />
  <br>
  <br>
  <img  src="img/dp_4.png" width="100%" />
  <br>
  <br>
  <img  src="img/dp_5.png" width="100%" />
  <br>
  <br>
</center>

---

#### Result
<div class="container">
  <div class="column">
    <center>
      <h6>Original</h6>
      <img src="img/dp_1.png" width="100%" />
      <img src="img/dabby_1.png" width="75%" />
      <audio controls>
        <source src="mp3/dabby_1.mp3" type="audio/mpeg">
      Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
      <h6>Variation</h6>
      <img src="img/dp_6.png" width="100%" />
      <img src="img/dabby_2.png" width="75%" />
      <audio controls>
        <source src="mp3/dabby_2.mp3" type="audio/mpeg">
      Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>
 
| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ----- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| Original | C4 | C4 | G4 | G4 | A4 | A4 | G4 | F4 | F4 | E4 | E4 |s 
|Variation | E4 | G4 | G4 | A4 | E4 | F4 | F4 | F4 | F4 | E4 | E4 | 
| Difference | 3 | 5 | 0 | 1 | 4 | 3 | 1 | 0 | 0 | 0 | 0 |

---

#### Melodic Variation with Expanded Rhythm 
  <center>
  <h6>Original</h6>
    <img src="img/er_1.png" height="100px"  />
    <br>
    <img src="img/erp_1.png" height="75px"  />
    <br>
  </center>
  <center>
  <h6>Expanded Rhythm</h6>
    <img src="img/er_12.png" height="100px" />
    <br>
    <img src="img/note_expand.png" height="75px"  />
  </center>

---

#### Our Method
<section data-marpit-fragments="1">
  <div class="container">
    <div class="column">
      <center>
        <h6> Our Method Diagram</h6>
        <img src="img/our_method1.png" height="550px" />
      </center>
    </div>
    <div data-marpit-fragment="1" class="column">
      <center>
        <h6>Process in MVCM 1. - MVCM 5. </h6>
        <img src="img/our_method2.png" height="510px" />
      </center>
    </div>
  </div>
</section>


---

#### Our Method

<br>
<center>
<h6>Our Variation</h6>
  <br>
  <img src="img/erp_6.png" width="100%" />
  <br>
  <img src="img/er_2.png" width="75%" />
  <br>
  <audio controls>
    <source src="mp3/er_2.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

---

#### Our Result
<br>
<br>

Let $\displaystyle\{p_k\}_{k=0}^{m-1}$ being a sequence of musical pitches with expanded rhythms and $\{\phi_i(kh)\}_{k=0}^{m-1}$, where $\phi_i:\mathbb{R}_+ \to \mathbb{R}$ is a numerical solution in the $i$-th component of the chaotic system. We define a mapping $g$ as
$$
\begin{equation}
g(\phi_i(kh)) := p_k
\end{equation}
$$

---

#### Our Result
<br>

Let $\{\tilde{\phi}_i(kh)\}_{k=0}^{m-1}$ is a numerical solution with new initial condition in the $i$-th component of the chaotic system. We then define another mapping $l$ as:
$$
\begin{equation} 
l(\tilde{\phi}_i(kh)) :=
\begin{cases}
g(\phi_i(b)) & \text{if } \exists\; a, b \in \text{dom }\phi_i \text{ s.t. } \phi_i(a) < \tilde{\phi}_i(kh) \leq \phi_i(b) \\
& \text{and } \nexists\, c \in \text{dom }\phi_i\text{ s.t. } \phi_i(a) < \phi_i(c) \leq \phi_i(b) \\
g(\phi_i(a)) & \text{if } \tilde{\phi}_i(kh) < \phi_i(a) \text{ for all } a \in \text{dom }\phi_i \\
g(\phi_i(b)) & \text{otherwise}
\end{cases}
\end{equation}
$$

---

#### Examples from Expanded Rhythm 

<br>

<center>
Pachelbel - Canon in D
</center>

<div class="container">
  <div class="column">
    <center>
    <h6>Original</h6>
      <audio controls>
        <source src="mp3/original_cnd.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
    <h6>Variation</h6>
      <audio controls>
        <source src="mp3/new_cnd.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>

<br>

<center>
Yiruma, (이루마) - River Flows in You
</center>
<div class="container">
  <div class="column">
    <center>
    <h6>Original</h6>
      <audio controls>
        <source src="mp3/original_rfiy.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
    <h6>Variation</h6>
      <audio controls>
        <source src="mp3/new_rfiy.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>

---

#### Future Approach

<h6> Melodic variation </h6>
<img src="img/melodic_variation.png" width="100%" />
<h6> Rhythmic variation </h6>
<img src="img/rhythmic_variation.png" width="100%" />

---

<center>
<H1> Q&A </H1>
<br>
<img src="img/qrcode.png" width="35%" />
</center>
