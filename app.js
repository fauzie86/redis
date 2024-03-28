const redis = require('redis');

const client = redis.createClient({
    host: 'localhost',
    port: 6379
});

(async () =>{
    try{
        await client.connect();
        console.log('Connected to Redis server');

        // SET Operation
        await client.set('name', 'Sam');
        console.log('SET name = Sam');

        // GET Operation
        const value = await client.get('name');
        console.log('GET name:', value);

        //INCR operation
        await client.incr('counter');
        console.log('INCR counter');

        //DECR Operation
        await client.decr('counter');
        console.log('DECR counter');

        //DEL Operation
        await client.del('counter');
        console.log('DEL counter');
    } catch (error){
        console.log(error);
    }finally{
        await client.quit();
    }
})();