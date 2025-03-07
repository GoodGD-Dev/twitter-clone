import CryptoJS from 'crypto-js';

export const getAvatar = (email) => {
    return `https://robohash.org/${email.trim().toLowerCase()}?set=set4&size=40x40`;
}

export const getRandomImage = () => {
    const accessKey = 'your-unsplash-api-access-key';
    return `https://api.unsplash.com/photos/random?client_id=${accessKey}&w=600&h=400`;
}