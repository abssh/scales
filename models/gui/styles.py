
appbarStyle = {
    # Qfr
    "QFrame":  """
    QFrame{
        background-color: #ffdcab;
        border: none;   }
    """,
    # Qla
    "QLabel":
    """ 
    QLable{
        border: none;
        color: #222222;
        padding: 4px;
        font-family: "RobotoMono";
        font-size: 14px;
        }
    """,
    # Qpus
    "QPushButton":
    """
    QPushButton{ 
        border: none;
        font-size: 15px;
        font-style: italic;
    }QPushButton:hover{
        color: #888888;
          }
    """
}
bodyContentStyle = """
QToolTip{
    background-color: rgba(80, 80, 80, 0.3);
    color: white;
    border: none;
}
"""

noteChoiceButtonsUnselected = """
QLabel{ 
    border-radius: 17%;
    font-size: 15px;
    background-color: rgba(190, 190, 190, 0.5);
    
}QLabel:hover{
    background-color: rgba(210, 210, 210, 0.5);
}
"""
noteChoiceButtonsSelected= """
QLabel{ 
    border-radius: 17%;
    font-size: 15px;
    background-color: rgba(240, 60, 80, 0.8);

}QLabel:hover{
    background-color: rgba(255, 60, 80, 0.9);
}
"""

scaleChoiceButtonsUnselected = """
QLabel{ 
    border-radius: 17%;
    font-size: 15px;
    background-color: rgba(190, 190, 190, 0.5);
    
}QLabel:hover{
    background-color: rgba(210, 210, 210, 0.5);
}
"""
scaleChoiceButtonsSelected= """
QLabel{ 
    border-radius: 17%;
    font-size: 15px;
    background-color: rgba(240, 60, 80, 0.8);

}QLabel:hover{
    background-color: rgba(255, 60, 80, 0.9);
}
"""
