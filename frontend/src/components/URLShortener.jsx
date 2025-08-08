import React, { useState } from 'react';
import axios from 'axios';

const URLShortener = () => {
    const [inputUrl, setInputUrl] = useState('');
    const [shortUrl, setShortUrl] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError('');
        setShortUrl('');

        try {
            const response = await axios.post('http://localhost:8000/api/url', {
                original_url: inputUrl,
            });
            const shortCode = response.data.short_code;
            setShortUrl(`${window.location.origin}/${shortCode}`);
        } catch (err) {
            setError('Failed to shorten URL. Please check the URL and try again.');
            console.error(err);
        }

        setIsLoading(false);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="url"
                    value={inputUrl}
                    onChange={(e) => setInputUrl(e.target.value)}
                    placeholder="Enter URL to shorten"
                    required
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Shortening...' : 'Shorten'}
                </button>
            </form>

            {shortUrl && (
                <div>
                    <p>Shortened URL:</p>
                    <a href={shortUrl} target="_blank" rel="noopener noreferrer">
                        {shortUrl}
                    </a>
                </div>
            )}

            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default URLShortener;
