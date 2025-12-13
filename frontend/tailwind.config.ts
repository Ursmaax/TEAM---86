import type { Config } from "tailwindcss";

const config: Config = {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
        "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            colors: {
                background: "#0b0f1a",
                card: "#111827",
                border: "#1f2937",
                primary: "#3b82f6",
                text: {
                    primary: "#e5e7eb",
                    secondary: "#9ca3af"
                }
            },
        },
    },
    plugins: [],
};
export default config;
