function toss_head(request)
{
    var userchoiceHead=$('head1').val()
    var toss_result
    var prob = Math.random();
    if(prob==0)
    {
        toss_result='Head'
    }
    else
    {
        toss_result='Tail'
    }
    if(toss_result==userchoiceHead)
    {
        alert("yeah")
        document.getElementById('result').innerHTML="You won the toss!"
        
    }
    else{
        alert("You lost")
        document.getElementById('result').innerHTML="Computer won the toss and elected to bat first"
    }
    
}