document.getElementById('deleteOrderForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const orderNumber = document.getElementById('orderNumber').value;
    const orderAmount = document.getElementById('orderAmount').value;

    fetch('/deleteOrder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            order_number: orderNumber,
            order_amount: orderAmount // Currently not used in backend but can be passed for validation
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Order deleted successfully.');
            // Optionally, redirect to another page or refresh the orders list
        } else {
            alert('Error deleting order: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
