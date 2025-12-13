"use client";

import { useState } from "react";
// Removed Framer Motion imports
import { Shield, Plane, Activity, FileText, Globe, ArrowRight, Loader2 } from "lucide-react";

interface RiskReport {
    political_risk: string;
    schedule_risk: { delay_days: number; risk_level: string };
    trade_risk: string;
    logistics_risk: string;
    final_report: string;
    scores: Record<string, number>;
}

export default function Home() {
    const [formData, setFormData] = useState({
        product: "Semiconductors",
        origin: "Taiwan",
        destination: "Germany",
        mode: "Air Freight",
        planned_date: "2025-12-13",
        expected_date: "2025-12-13",
    });
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<RiskReport | null>(null);

    const handleAnalyze = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setResult(null);

        try {
            const res = await fetch("http://localhost:8000/analyze", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ ...formData, demo_mode: true }),
            });
            const data = await res.json();
            setResult(data);
        } catch (err) {
            console.error(err);
            alert("Error: Ensure Backend is running on Port 8000");
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="min-h-screen p-8 max-w-4xl mx-auto">
            {/* HEADER */}
            <div className="mb-8 border-b border-gray-800 pb-6">
                <div className="flex items-center gap-3 mb-2">
                    <Globe className="w-6 h-6 text-blue-500" />
                    <h1 className="text-2xl font-bold text-white">RiskWise AI</h1>
                </div>
                <p className="text-gray-400">Supply Chain Risk Assessment Platform</p>
            </div>

            {/* INPUT FORM */}
            <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-6 mb-8">
                <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
                    <Activity className="w-5 h-5 text-blue-500" />
                    Analysis Request
                </h2>

                <form onSubmit={handleAnalyze} className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="space-y-2">
                        <label className="text-sm font-medium text-gray-400">Product</label>
                        <input
                            className="w-full bg-[#0b0f1a] border border-[#1f2937] rounded p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                            value={formData.product}
                            onChange={(e) => setFormData({ ...formData, product: e.target.value })}
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="text-sm font-medium text-gray-400">Transport Mode</label>
                        <select
                            className="w-full bg-[#0b0f1a] border border-[#1f2937] rounded p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                            value={formData.mode}
                            onChange={(e) => setFormData({ ...formData, mode: e.target.value })}
                        >
                            <option>Air Freight</option>
                            <option>Sea Freight</option>
                            <option>Rail Freight</option>
                            <option>Road Transport</option>
                        </select>
                    </div>

                    <div className="space-y-2">
                        <label className="text-sm font-medium text-gray-400">Origin</label>
                        <input
                            className="w-full bg-[#0b0f1a] border border-[#1f2937] rounded p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                            value={formData.origin}
                            onChange={(e) => setFormData({ ...formData, origin: e.target.value })}
                        />
                    </div>

                    <div className="space-y-2">
                        <label className="text-sm font-medium text-gray-400">Destination</label>
                        <input
                            className="w-full bg-[#0b0f1a] border border-[#1f2937] rounded p-3 text-white focus:ring-2 focus:ring-blue-500 outline-none"
                            value={formData.destination}
                            onChange={(e) => setFormData({ ...formData, destination: e.target.value })}
                        />
                    </div>

                    <div className="md:col-span-2 pt-2">
                        <button
                            disabled={loading}
                            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-md w-full md:w-auto flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                        >
                            {loading && <Loader2 className="w-4 h-4 animate-spin" />}
                            {loading ? "Analyzing..." : "Run Analysis"}
                        </button>
                    </div>
                </form>
            </div>

            {/* RESULTS */}
            {result && (
                <div className="space-y-6">
                    {/* Summary */}
                    <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-6">
                        <div className="flex items-center gap-2 mb-4 text-blue-400">
                            <FileText className="w-5 h-5" />
                            <h3 className="font-semibold uppercase text-sm tracking-wide">Executive Summary</h3>
                        </div>
                        <div className="text-gray-300 leading-relaxed whitespace-pre-wrap">
                            {result.final_report}
                        </div>
                        <div className="mt-6 pt-6 border-t border-[#1f2937] flex justify-between items-center">
                            <span className="text-gray-400">Total Risk Score</span>
                            <span className="text-2xl font-bold text-white">
                                {Object.values(result.scores).reduce((a, b) => a + b, 0)}
                                <span className="text-gray-500 text-lg font-normal">/20</span>
                            </span>
                        </div>
                    </div>

                    {/* Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-4">
                            <h4 className="text-gray-400 text-sm font-medium mb-2">Political Stability</h4>
                            <p className="text-white">{result.political_risk}</p>
                        </div>
                        <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-4">
                            <h4 className="text-gray-400 text-sm font-medium mb-2">Schedule Risk</h4>
                            <p className="text-white">Delay: {result.schedule_risk.delay_days} days</p>
                            <p className="text-gray-400 text-sm">{result.schedule_risk.risk_level}</p>
                        </div>
                        <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-4">
                            <h4 className="text-gray-400 text-sm font-medium mb-2">Trade Compliance</h4>
                            <p className="text-white">{result.trade_risk}</p>
                        </div>
                        <div className="bg-[#111827] border border-[#1f2937] rounded-lg p-4">
                            <h4 className="text-gray-400 text-sm font-medium mb-2">Logistics</h4>
                            <p className="text-white">{result.logistics_risk}</p>
                        </div>
                    </div>
                </div>
            )}
        </main>
    );
}
