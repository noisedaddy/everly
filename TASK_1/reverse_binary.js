  
    function reverseNum(n) {

        let reversed = n.toString().split("").reverse().join("");

        //from string to integer
        reversed = parseInt(reversed);

        if (n < 0) {
            return reversed * -1;
        }

        return Number(reversed);
    }


    const number = parseInt(prompt('Enter a decimal number: '));

    // convert to binary
    const result = number.toString(2);

    //reverse bits
    var final = reverseNum(result);
    alert(parseInt(final, 2));

