
# coding: utf-8

# In[1]:

import numpy as np
from vispy import app
from vispy import gloo


# In[2]:

c = app.Canvas(keys='interactive')
vertex = """
attribute vec2 a_position;
void main (void)
{
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""
fragment = """
void main()
{
    gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
}
"""


# In[3]:

program = gloo.Program(vertex, fragment)


# In[4]:

program['a_position'] = np.c_[
        np.linspace(-1.0, +1.0, 1000),
        np.random.uniform(-0.5, +0.5, 1000)].astype(np.float32)


# In[5]:

@c.connect
def on_resize(event):
    gloo.set_viewport(0, 0, *event.size)
@c.connect
def on_draw(event):
    gloo.clear((1,1,1,1))
    program.draw('line_strip')
c.show()
app.run();

